import ipaddress

import click
import ovh
from tabulate import tabulate

# create a client
client = ovh.Client()


@click.group()
def cli():
    pass


@cli.group(invoke_without_command=True)
@click.pass_context
def server(ctx):
    if ctx.invoked_subcommand is None:
        servers = client.get('/dedicated/server')
        click.echo(tabulate(([s] for s in servers), headers=(['Name'])))


@server.command()
@click.option('--service')
def virtualmacs(service):
    table = []
    vmacs = client.get('/dedicated/server/%s/virtualMac' % service)
    for vmac in vmacs:
        ips = client.get('/dedicated/server/%s/virtualMac/%s/virtualAddress' % (service, vmac))
        table.append([
            ipaddress.ip_address(ips[0]),
            vmac,
        ])
    table.sort(key=lambda x: x[0])
    print(tabulate(table, headers=['IP', 'MAC']))


@server.command()
@click.option('--service')
@click.option('--ip')
@click.option('--name', default='vm')
def create_mac(service, ip, name):
    res = client.post('/dedicated/server/%s/virtualMac' % service,
                      ipAddress=ip,
                      type='ovh',
                      virtualMachineName=name)
    click.echo(res)
