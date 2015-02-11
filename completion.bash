_taksman_complete() {
  COMPREPLY=()
  local word="${COMP_WORDS[COMP_CWORD]}"
  local completions="$(ls -1 "$HOME"/.taksman/entries)"
  COMPREPLY=( $(compgen -W "$completions" -- "$word") )
}

complete -F _taksman_complete taksman
