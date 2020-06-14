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
    firefox
    slack
    atom
    dashlane
    expressvpn
    itsycal
    macs-fan-control
    keka
    whatsapp
    google-photos-backup-and-sync
    slack
    rescuetime
    cold-turkey-blocker
    omnidisksweeper
    cleanmymac
    zoomus
    balenaetcher
    calibre
    rstudio
    chrome
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
# Settings set up

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

echo "lemme copy stuff from quick looks into files"
defaults write com.apple.finder QLEnableTextSelection -bool TRUE

echo "Show me all connected drives, folders, networks on desktop"
defaults write com.apple.finder ShowExternalHardDrivesOnDesktop -bool true

echo "make time machine stop annoying me trying to hijack every hard drive i plug in"
defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true

echo "Setting up mouse settings.."
defaults write com.apple.AppleMultitouchMouse MouseButtonMode -string "OneButton"
defaults write com.apple.AppleMultitouchMouse MouseOneFingerDoubleTapGesture -int 0
defaults write com.apple.AppleMultitouchMouse MouseTwoFingerDoubleTapGesture -int 3
defaults write com.apple.AppleMultitouchMouse MouseTwoFingerHorizSwipeGesture -int 2

defaults write com.apple.AppleMultitouchTrackpad SecondClickThreshold -int 1
defaults write com.apple.AppleMultitouchTrackpad TrackpadCornerSecondaryClick -int 0
defaults write com.apple.AppleMultitouchTrackpad TrackpadFiveFingerPinchGesture -int 2
defaults write com.apple.AppleMultitouchTrackpad TrackpadFourFingerHorizSwipeGesture -int 2
defaults write com.apple.AppleMultitouchTrackpad TrackpadFourFingerPinchGesture -int 2
defaults write com.apple.AppleMultitouchTrackpad TrackpadFourFingerVertSwipeGesture -int 2
defaults write com.apple.AppleMultitouchTrackpad TrackpadHandResting -bool true
defaults write com.apple.AppleMultitouchTrackpad TrackpadPinch -int 1
defaults write com.apple.AppleMultitouchTrackpad TrackpadRightClick -bool true
defaults write com.apple.AppleMultitouchTrackpad TrackpadThreeFingerDrag -bool true



####################################
# Dock related scripts 

echo "Change the size of dock icons"
defaults write com.apple.dock tilesize -int 36

echo "Remove all the default icons from the dock lmaoooo"
defaults write com.apple.dock persistent-apps -array

echo "Don't animate movement when stuff is opened from the dock"
defaults write com.apple.dock launchanim -bool false

echo "Auto-hide dock"
defaults write com.apple.dock autohide -bool true

echo "Expose group applications"
defaults write com.apple.dock expose-group-apps -bool true

echo "Turn magnification off"
defaults write com.apple.dock magnification -bool false

echo "Change orientation of the dock to the left"
defaults write com.apple.dock orientation -string "left"

echo "Makes a recent items stack in the dock"
defaults write com.apple.dock persistent-others -array-add '{"tile-data" = {"list-type" = 1;}; "tile-type" = "recents-tile";}';

echo "Changing size of dick icons"
defaults write com.apple.dock tilesize -int 36

######################################
# Hot corners 

echo "Setting top right hot corner as lock"

defaults write com.apple.dock wvous-tr-corner -int 5
defaults write com.apple.dock wvous-tr-modifier -int 0

echo "Setting up bottom right hot corner as sleep"
defaults write com.apple.dock wvous-bl-corner -int 10
defaults write com.apple.dock wvous-bl-modifier -int 0

######################################3
# Misc settings

# Todo: Figure out installing addons automatically in firefox (deploying with autoconfig.js?)
# Todo: Figure out automatically importing BTT settings
# 
