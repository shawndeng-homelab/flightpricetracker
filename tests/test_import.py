"""Import Test."""

import importlib
import pkgutil

import flightpricetracker # noqa

def test_imports():
    """Test import modules."""
    prefix = "{}.".format(flightpricetracker.__name__) # noqa
    iter_packages = pkgutil.walk_packages(
        flightpricetracker.__path__,  # noqa
        prefix,
    )
    for _, name, _ in iter_packages:
        module_name = name if name.startswith(prefix) else prefix + name
        importlib.import_module(module_name)