import random_generator

our_random_number = random_generator.generate_random_number()
print("our random number is: ", str(our_random_number))

user_was_wrong = True

while(user_was_wrong):
    user_guess = random_generator.get_user_guess()
    print("The users guess was: ", str(user_guess))
    user_was_wrong = random_generator.was_answer_correct(our_random_number, user_guess)
    if user_was_wrong:
        random_generator.give_user_a_hint(our_random_number, user_guess)
