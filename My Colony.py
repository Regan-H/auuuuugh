countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
print("Welcome to the countries of Africa game")
input("press anything to start\n")
score = 0
lives = 3
while len(countries)>0:
    if lives<1:
         break
    else:
        print(f"You have {len(countries)} countries left to guess\n score={score} lives:{lives}")
        guessp= input("insert africian country here\n")
        guess= guessp[0].upper()+guessp[1:]
        if guess in countries:
            print("Good guess")
            score= score+1
            countries.remove(guess)
        elif guess not in countries:
            print("bad guess")
            lives= lives-1
if len(countries)==0:
    print("You win")
elif lives<=0:
    print("You lose")