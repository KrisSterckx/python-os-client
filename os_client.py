from os import environ as env
from neutronclient.v2_0 import client as neutronclient


class OsClient:
    def __init__(self):
        self.neutron = None
        self.authenticate()

    @staticmethod
    def get_env_var(name):
        try:
            return env[name]
        except KeyError:
            print name + " not defined."
            exit(-1)

    def authenticate(self):
        self.neutron = neutronclient.Client(auth_url=self.get_env_var('OS_AUTH_URL'),
                                            username=self.get_env_var('OS_USERNAME'),
                                            password=self.get_env_var('OS_PASSWORD'),
                                            tenant_name=self.get_env_var('OS_TENANT_NAME'))

        print '\nneutron authentication OK.'

    def sample_flow(self):
        # create network
        network_resp = self.neutron.create_network({'network': {'name': 'kris'}})
        print "neutron network created:", network_resp
        network = network_resp['network']

        # delete network
        self.neutron.delete_network(network['id'])
        print "neutron network deleted."


if __name__ == "__main__":
    OsClient().sample_flow()

