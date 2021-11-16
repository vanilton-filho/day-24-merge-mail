class MergeEmail:

    def __init__(self, file, file_output_folder):
        self.output = file_output_folder
        with open(f"{file}") as letter:
            self.starting_letter = letter.read()

    def replace_pattern(self, file, pattern):
        with open(f"{file}") as src:
            recipient = src.readline()
            while recipient:
                recipient = recipient.strip()
                new_email = self.starting_letter
                new_email = new_email.replace(pattern, recipient)
                self.create_new_email(new_email, recipient)

                print(f"New email for {recipient} created!")
                recipient = src.readline()

    def create_new_email(self, new_letter, recipient):
        with open(f"{self.output}/letter_for_{recipient.lower()}.txt", mode="w") as ready_letter:
            ready_letter.write(new_letter)
