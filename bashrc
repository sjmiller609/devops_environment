# Path to the bash it configuration
export BASH_IT="$HOME/.bash_it"

# Lock and Load a custom theme file
# location /.bash_it/themes/
export BASH_IT_THEME='bobby'

# Your place for hosting Git repos. I use this for private repos.
export GIT_HOSTING='git@github.com'

# Don't check mail when opening terminal.
unset MAILCHECK

# Change this to your console based IRC client of choice.
export IRC_CLIENT='irssi'

# Set this to the command you use for todo.txt-cli
export TODO="t"

# Set this to false to turn off version control status 
# checking within the prompt for all themes
# I disabled this because it causes slight lag 
# when in repository with many commits
export SCM_CHECK=false

# Load Bash It
source "$BASH_IT"/bash_it.sh

# Aliases for 'cago'
alias cagol='source /usr/local/bin/cago.sh list'
alias cagor='source /usr/local/bin/cago.sh refresh'
alias cagos='source /usr/local/bin/cago.sh switch'
alias cagou='source /usr/local/bin/cago.sh unset'

# These environment variables important for tmux style
# and git editor choice
export TERM=xterm-256color
export EDITOR=vim
export VISUAL=vim
