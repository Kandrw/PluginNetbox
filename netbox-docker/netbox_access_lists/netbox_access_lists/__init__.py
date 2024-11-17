from netbox.plugins import PluginConfig



# class NetBoxAccessListsConfig(PluginConfig):
#     name = 'netbox-access-lists'
#     verbose_name = ' NetBox Access Lists'
#     description = 'Manage simple ACLs in NetBox'
#     version = '0.1'
#     base_url = 'access-lists'


class NetBoxAccessListsConfig(PluginConfig):
    name = 'netbox_access_lists'
    verbose_name = ' super plugin'
    description = 'simple plugin'
    version = '0.1'
    base_url = 'access-lists'




config = NetBoxAccessListsConfig