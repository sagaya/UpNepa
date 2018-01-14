from pip.commands.install import InstallCommand
from pip.baseparser import ConfigOptionParser
from pip.exceptions import PipError
from pip.utils import get_prog
import logging

logger = logging.getLogger(__name__)
install_cmd = InstallCommand()


def pip_install(package_name):
    parser_kw = {
        'usage': install_cmd.usage,
        'prog': '%s %s' % (get_prog(), install_cmd.name),
        'formatter': None,
        'add_help_option': False,
        'name': install_cmd.name,
        'description': install_cmd.__doc__,
        'isolated': False,
    }

    parser = ConfigOptionParser(**parser_kw)
    options, args = parser.parse_args(["install", package_name])
    try:
        status = install_cmd.run(options, args)
        if isinstance(status, int):
            logger.debug("Returned status code: {status}".format(status=status))
            return status == 0
    except (PipError, KeyboardInterrupt) as exc:
        logger.critical(str(exc))
        logger.debug('Exception information:', exc_info=True)
        return False
    except:
        logger.critical('Exception:', exc_info=True)
        return False
    return True
