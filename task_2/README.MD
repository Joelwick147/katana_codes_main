This is a simple Flask web application that checks whether a given word or phrase is a palindrome (a string that reads the same forward and backward). It shows a history of recent checks.

Features

- Built with Flask
- Styled using Bootstrap 5
- Checks if text is a palindrome (ignores case and punctuation)
- Shows the last 5 palindrome checks
- Ready for deployment on Vercel

How It Works

1. User enters text into the form.
2. Text is cleaned (lowercased, non-alphanumeric removed).
3. App compares the cleaned string to its reverse.
4. Displays whether it's a palindrome.
5. Saves the result in a temporary in-memory history list.

Examples of words for reference

hanah,
121,
no lemon, no melon,
was it a car or a cat i saw,
racecar
