# %%
# ! pip install git+https://github.com/vga-team/python-helper.git
# ! pip install git+https://github.com/vga-team/gwf-vis-python-helper.git

# %% import
import vga
from gwfvis import conf as gwfvisconf
import json

# %% config
vis_config = gwfvisconf.create_config()
vga.set_view(vis_config, center=[51, -115], zoom=5)

# %% setup data provider
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvisconf.PluginNames.SQLITE_LOCAL_DATA_PROVIDER)
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvisconf.PluginNames.GWFVISDB_DATA_PROVIDER)

# %% add U15 layer
data_source = 'gwfvisdb:https://gwf-vis.usask.ca/assets/datasets/u15.gwfvisdb'
u15_layer = vga.add_plugin(
    config=vis_config, name=gwfvisconf.PluginNames.GEOJSON_LAYER)
vga.set_plugin_props(
    u15_layer,
    {
        'displayName': 'U15',
        'layerType': 'overlay',
        'active': True,
        'pointMode': 'pushpin'
    }
)
# %% add data control
data_control = vga.add_plugin(
    config=vis_config, name=gwfvisconf.PluginNames.DATA_CONTROL, container='main', props={
        'dataSources': [data_source],
        'dataSourceDict': {'U15': data_source}
    }
)

# %% add metadata
metadata = vga.add_plugin(
    config=vis_config, name=gwfvisconf.PluginNames.METADATA, container='sidebar', container_props={'slot': 'top'})

# %% option1: print the config JSON
print(json.dumps(vis_config))

# %% option2: print the URL
print(vga.generate_vis_url(vis_config))

# %%
