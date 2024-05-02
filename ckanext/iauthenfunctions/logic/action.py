import ckan.plugins.toolkit as tk
import ckanext.iauthenfunctions.logic.schema as schema


@tk.side_effect_free
def iauthenfunctions_get_sum(context, data_dict):
    tk.check_access(
        "iauthenfunctions_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.iauthenfunctions_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'iauthenfunctions_get_sum': iauthenfunctions_get_sum,
    }
