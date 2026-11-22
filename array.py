import sys

def get_scores():
    if len(sys.argv) > 1:
        return [float(x) for x in sys.argv[1:]]
    
    scores_input = input("Enter scores separated by space: ")
    return [float(score) for score in scores_input.split()]

if __name__ == "__main__":
    scores = get_scores()
    if not scores:
        print("No scores provided.")
    else:
        total = sum(scores)
        avg = total / len(scores)
        maximum = max(scores)
        minimum = min(scores)
        
        print(f"Scores: {scores}")
        print(f"Sum: {total}")
        print(f"Average: {avg:.2f}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")