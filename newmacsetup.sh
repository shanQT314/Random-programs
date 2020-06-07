echo "Seting up Macbook..."

echo "Please enter administrator password: "
sudo -v

while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

echo "Installing all x-code related materials.."
xcode-select --install 

echo "Checking if Homebrew is installed"
if test ! $(which brew); then
    echo "Homebrew is not installed. Downloading it..."
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi 

echo "Updating brew.."
brew update 
brew upgrade --all 

echo "Installing Git.."
brew install git 

#Todo: Add some way to get all Git settings set up here 

echo "Installing svn.."
brew install svn 

echo "Installing node.."
brew install node

echo "Removing outdated versions from brew.."
brew cleanup 

#Need Moe's Zsh set up for this 

echo "Installing OMZ! (Oh my Zsh)"
curl -L http://install.ohmyz.sh | sh

# Setting up list of Applications to install using cask 
brew install caskroom/cask/brew-cask

applications = (
    1password
    alfred
    spotify
    iterm2
    atom
    vlc
    bettertouchtool
    brave-browser
    slack
)

brew cask install --appdir="/Applications" ${applications[@]}

brew cask cleanup
brew cleanup 

echo "Installing Python 3"
brew install python3

#################################

echo "Installing JS related applications" 

npm install -g coffee-script
npm install -g jshint 


###################################
# Optional, remove or add as per Need

echo "Disabling start up sound effects"
sudo nvram SystemAudioVolume=" "

echo "Enable requiring password right after sleep or lock or screensaver vibes"
defaults write com.apple.screensaver askForPassword -int 1
defaults write com.apple.screensaver askForPasswordDelay -int 0

echo "Show hidden files always"
defaults write com.apple.finder AppleShowAllFiles -bool true

echo "Show extensions" 
defaults write NSGlobalDomain AppleShowAllExtensions -bool true

echo "Show path location at the bottom of the finder" 
defaults write com.apple.finder ShowPathbar -bool true

echo "ALWAYS SEARCH CURRENT FOLDER FIRST"
defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"

echo "Remove warning when changing an extension lol"
defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false

echo "Change the size of dock icons"
defaults write com.apple.dock tilesize -int 36

echo "Remove all the default icons from the dock lmaoooo"
defaults write com.apple.dock persistent-apps -array

echo "Don't animate movement when stuff is opened from the dock"
defaults write com.apple.dock launchanim -bool false

echo "Auto-hide dock"
defaults write com.apple.dock autohide -bool true

# Not sure if you use hot corners, but I do so here is what I have tbh
echo "Setting top right hot corner as lock"

defaults write com.apple.dock wvous-tr-corner -int 5
defaults write com.apple.dock wvous-tr-modifier -int 0

echo "Setting up bottom right hot corner as sleep"
defaults write com.apple.dock wvous-bl-corner -int 10
defaults write com.apple.dock wvous-bl-modifier -int 0

