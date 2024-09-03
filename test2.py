import os

def check_path(path):
    # Check if the path exists
    if os.path.exists(path):
        print(f"The path exists: {path}")
        
        # Check if it's a directory
        if os.path.isdir(path):
            print("It's a directory. Listing all files:")
            # List all files and subdirectories in the path
            for root, dirs, files in os.walk(path):
                for file in files:
                    print(os.path.join(root, file))
        else:
            print("It's a file.")
    else:
        print(f"The path does not exist: {path}")

if __name__ == "__main__":
    # Replace this with the path you want to test
    path_to_check = r"C:\Users\ifran\OneDrive\Desktop\Dev\GenAI\Udemy LangChain GenAI Course\ragchain-langchain-docs\langchain-docs\api.python.langchain.com\en\latest"
    
    check_path(path_to_check)