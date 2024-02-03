import os

def get_linux_distribution():
    lsb_release = os.getenv('LSB_RELEASE')
    
    if lsb_release:
        return lsb_release

    # Check /etc/os-release file for distribution identification
    try:
        with open('/etc/os-release', 'r') as f:
            lines = f.readlines()
            distro_info = {}
            for line in lines:
                key, value = line.strip().split('=', 1)
                distro_info[key] = value.strip('"\'')

            return distro_info.get('ID', None)
    except FileNotFoundError:
        pass

    return None

def update_system(package_manager):
    if package_manager:
        if package_manager == 'apt':
            os.system('sudo apt update && sudo apt upgrade -y')
        elif package_manager == 'dnf':
            os.system('sudo dnf check-update && sudo dnf upgrade -y')
        elif package_manager == 'yum':
            os.system('sudo yum check-update && sudo yum upgrade -y')
        elif package_manager == 'pacman':
            os.system('sudo pacman -Syu')
        # Add more update commands as needed
        else:
            print(f'Update command not found for {package_manager} package manager.')

def get_package_manager(distribution):
    package_managers = {
        'debian': 'apt',
        'ubuntu': 'apt',
        'fedora': 'dnf',
        'centos': 'yum',
        'arch': 'pacman'
        # Add more mappings as needed
    }

    return package_managers.get(distribution, None)


if __name__ == '__main__':
    distribution = get_linux_distribution()

    if distribution:
        print(f'Linux distribution: {distribution}')
        package_manager = get_package_manager(distribution)
        if package_manager:
            print(f'Package manager: {package_manager}')
            update_system(package_manager)
        else:
            print('Package manager not found for the given distribution.')
    else:
        print('Unable to determine Linux distribution.')
