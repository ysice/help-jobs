pip list --outdated --format=freeze | awk -F '=' '{print $1}' | xargs pip install --upgrade
