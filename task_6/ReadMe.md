Square Sums Row Finder

A web application built with Flask that finds a sequence of numbers from `1` to `n` (where `2 ≤ n ≤ 43`) such that the sum of every pair of adjacent numbers is a perfect square.

Features

- Enter any integer from 2 to 43.
- See a sequence where adjacent numbers sum to a perfect square (if it exists).
- Clean, responsive Bootstrap UI.

How It Works

The app uses backtracking to search for a valid permutation of numbers where each adjacent pair sums to a perfect square.

Example:

Input: n = 15
Output: 8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9

Technologies

- Python 3.x
- Flask
- HTML5 + Bootstrap 5

Installation

1.Clone the repo:
git clone [https://github.com/your-username/square-sums-row.git](https://github.com/Joelwick147/katana_codes_main/tree/main/task_6)
cd square-sums-row

2. Create virtual environment:
   python -m venv venv
   source venv/bin/activate Or On Windows: venv\Scripts\activate

3. Install dependencies:

   pip install flask

4. Run the app:

   python app.py
