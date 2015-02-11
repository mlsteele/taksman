_taksman_complete() {
  local word completions
  word="$1"
  completions="$(ls -1 $HOME/.taksman/entry)"
  reply=( "${(ps:\n:)completions}" )
}

compctl -K _taksman_complete taksman
