import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def iauthenfunctions_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "iauthenfunctions_get_sum": iauthenfunctions_get_sum,
    }
