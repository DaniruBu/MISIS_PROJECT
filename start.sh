echo "Initialising Git ..." &&
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        apt-get install git-flow
elif [[ "$OSTYPE" == "darwin"* ]]; then
        if ! brew -v | grep -q "Homebrew"
        then /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew -v && brew install git-flow
fi
echo "Initialising Gitflow ..." &&
echo "Проведите настройку Gitflow:" &&
git flow init &&
pip install --upgrade pip && 
pip install -r /temp/requirements.txt &&
pre-commmit install &&
git config --unset-all core.hooksPath