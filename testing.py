# -*- coding: utf-8 -*-
# %%
from rich import print
from pathlib import Path
from spl.__main__ import SplManager
import splunk_appinspect

# %%
spl = SplManager(src="nxtp-onprem", dest="localhost", interactive=False)

# %%
print(
    "Properties: ",
    [prop for prop in dir(spl.sync.src.client) if not prop.startswith("_") and prop.endswith("s")],
)  # and prop.endswith("s")])
# %%
print(
    "Apps: ", [app.name for app in spl.sync.src.client.apps.list() if not app.name.startswith("_")]
)
print(
    {
        app.name: {"access": app.access, "content": app.content}
        for app in spl.sync.src.client.apps.list()
    }
)

# %%

"test" in {"test1": 123, "asdf": 989}.keys()


# %%
print(
    "Indexes: ",
    [index.name for index in spl.sync.src.client.indexes.list() if not index.name.startswith("_")],
)
print("Index properties: ", spl.sync.src.client.indexes["aks_logs"].__dict__)
# %%
print(
    "Users: ",
    [user.name for user in spl.sync.src.client.users.list() if not user.name.startswith("_")],
)
print("User properties: ", spl.sync.src.client.users["analytics"].__dict__)

# %%
print(
    "Roles: ",
    [role.name for role in spl.sync.src.client.roles.list() if not role.name.startswith("_")],
)
print("Role properties: ", spl.sync.src.client.roles["developer"].__dict__)

# %%
roles = spl.sync.src.client.roles
roles["developer"].name


# %%
print(
    "Saved searches: ",
    [
        saved_search.name
        for saved_search in spl.sync.src.client.saved_searches.list()
        if not saved_search.name.startswith("_")
    ],
)
print("Saved search properties: ", spl.sync.src.client.saved_searches["User Add"].__dict__)

# %%
spl.sync.src.namespace(sharing="app", owner="admin", app="Splunk_TA_windows", context=False)

# %%
print(
    "Event types: ",
    [
        event_type.name
        for event_type in spl.sync.src.client.event_types.list()
        if not event_type.name.startswith("_")
    ],
)
print("Event type properties: ", spl.sync.src.client.event_types["linux_audit_anomalies"].__dict__)

# %%
print("Capabilities: ", spl.sync.src.client.capabilities)

# %%
spl.sync.dest.client.capabilities

# %%
spl.sync.src.client.users["analytics"].__dict__

# %%
spl.sync.src.client.roles["redbull"]

# %%
import splunk_appinspect

# %%
app = splunk_appinspect.App(location="../../../apps/FortiEDR_TA_nxtp", python_analyzer_enable=False)
app

# %%
# splunk_appinspect.main.validate(["../../../apps/FortiEDR_App_nxtp"])
# %%
client = spl.sync.dest.client

# %%
client.namespace


import splunklib.binding as spl_context

# %%
# %%
from rich import print

from spl.__main__ import SplManager

spl = SplManager(src="nxtp-onprem", dest="localhost", interactive=False)
client = spl.sync.src.client
default_namespace = client.namespace


# %%
sync = spl.sync

# %%
manager = spl.manager(conn="nxtp-onprem")

# %%
manager.namespace(context=True, app="Splunk_SOCToolkit")


# %%
manager.saved_searches.generate()

# %%
client.namespace = default_namespace

# %%
client.namespace = spl_context.namespace(
    sharing="app",
    app="Splunk_SOCToolkit",
    owner=None,
)

# %%
print(
    [
        saved_search.name
        for saved_search in client.saved_searches.list()
        if saved_search.access.app == "Splunk_SOCToolkit"
    ]
)


# %%
apps =spl.apps(path=Path("../../apps"),name="*")
apps

# %%
my_apps = apps._apps
# %%
my_apps[0].__dict__


# %%
app = splunk_appinspect.App(location=Path("../../apps/Defender_TA_nxtp"),
python_analyzer_enable=False, 
trusted_libs_manager=False)

# %%
my_apps.sort(key = lambda x : x.package_id)
[app.package_id for app in my_apps]






# %%
from rich import print
from pathlib import Path
from spl.__main__ import SplManager
import splunk_appinspect

# %%
spl = SplManager(src="rb-onprem", dest="localhost", interactive=False)

# %%
client = spl._src.client


# %%
[ index.name for index in client.indexes.list() ]


# %%
client.namespace['app'] = "SPLUNK_GLOBAL_INDEXROUTING"

