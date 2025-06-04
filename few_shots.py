few_shots = [
    {
        "Question": "Which team won the most matches in 2020?",
        "SQLQuery": """
            SELECT winner, COUNT(*) AS wins
            FROM matches
            WHERE season = '2020'
            GROUP BY winner
            ORDER BY wins DESC
            LIMIT 1;
        """,
        "SQLResult": "Result of the SQL query",
        "Answer": "Mumbai Indians won the most matches in 2020."
    },
    {
        "Question": "How many runs did Virat Kohli score in match 335982?",
        "SQLQuery": """
            SELECT SUM(batsman_runs) 
            FROM deliveries 
            WHERE match_id = 335982 AND batsman = 'V Kohli';
        """,
        "SQLResult": "Result of the SQL query",
        "Answer": "Virat Kohli scored 45 runs."
    }
    # Add more based on different types of questions!
]