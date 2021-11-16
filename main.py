from merge_email import MergeEmail

merge_email = MergeEmail("Input/Letters/starting_letter.txt", "Output/ReadyToSend")
merge_email.replace_pattern(file="Input/Names/invited_names.txt", pattern="[name]")
