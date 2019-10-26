#/bin/sh

_notes_completions()
{
    local cur prev opts
    COMPREPLY=() 
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="new search open"      
    
    if [[ ${COMP_CWORD} == '1' ]] ; then         
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )         
        return 0     
    elif [[ $prev == open ]]; then
        COMPREPLY=($(compgen -W "$(ls /home/hunter/Documents/notes_taking_script/notes/)" -- $cur))
    elif [[ ${COMP_CWORD} == '3' ]] && [[ "${COMP_WORDS[1]}" == "open" ]] && [[ -d "/home/hunter/Documents/notes_taking_script/notes/${prev}" ]]; then 
        COMPREPLY=($(compgen -W "$(ls /home/hunter/Documents/notes_taking_script/notes/${prev})" -- $cur))
    elif [[ ${COMP_CWORD} == '2' ]] && [[ "${COMP_WORDS[1]}" == "new" ]]; then 
        COMPREPLY=($(compgen -W "$(ls /home/hunter/Documents/notes_taking_script/notes/)" -- $cur))
    fi

}

complete -F _notes_completions notes