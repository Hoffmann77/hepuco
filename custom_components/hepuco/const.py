"""The enphase_envoy component."""

from homeassistant.const import Platform


DOMAIN = "hepuco"

PLATFORMS = [Platform.SENSOR, Platform.BINARY_SENSOR]

ICON = "mdi:flash"

COORDINATOR = "coordinator"

NAME = "name"

CONF_PV_POWER = "pv_power_sensor"
CONF_GRID_EXPORT = "grid_export_sensor"

CONF_POWER_HP = "power_heat_pump"

CONF_TRESHOLD_0 = "treshold_0°C"
CONF_TRESHOLD_10 = "treshold_10°C"
CONF_TRESHOLD_20 = "treshold_20°C"



CONF_SERIAL_NUM = "serial_num"
CONF_USE_TOKEN_AUTH = "use_token_auth"
CONF_TOKEN_RAW = "token_raw"
CONF_CACHE_TOKEN = "cache_token"
CONF_EXPOSE_TOKEN = "expose_token"
CONF_EXPOSURE_PATH = "exposure_path"
CONF_DATA_UPDATE_INTERVAL = "data_update_interval"
CONF_GET_INVERTERS = "get_inverters"
CONF_ENCHARGE_ENTITIES = "encharge_entities"
CONF_USE_LEGACY_NAME = "use_lagacy_name"
CONF_INVERTERS = "inverters_config"
