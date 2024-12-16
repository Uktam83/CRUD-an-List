# Matrix CRUD Operations Example

def create_matrix(rows, cols):
    """Create a matrix by taking user input."""
    matrix = []
    print("Enter the elements row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} elements.")
            row = list(map(int, input(f"Re-enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def read_matrix(matrix):
    """Display the matrix."""
    print("\nCurrent Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))


def update_matrix(matrix):
    """Update a specific element in the matrix."""
    try:
        row = int(input("\nEnter the row index to update (0-based): "))
        col = int(input("Enter the column index to update (0-based): "))
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            new_value = int(input("Enter the new value: "))
            matrix[row][col] = new_value
            print(f"Updated element at ({row}, {col}) to {new_value}.")
        else:
            print("Invalid row or column index!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")


def delete_row_or_column(matrix):
    """Delete a specific row or column."""
    choice = input("\nDo you want to delete a row or column? (row/column): ").strip().lower()
    try:
        if choice == "row":
            row = int(input("Enter the row index to delete (0-based): "))
            if 0 <= row < len(matrix):
                del matrix[row]
                print(f"Deleted row {row}.")
            else:
                print("Invalid row index!")
        elif choice == "column":
            col = int(input("Enter the column index to delete (0-based): "))
            if 0 <= col < len(matrix[0]):
                for row in matrix:
                    del row[col]
                print(f"Deleted column {col}.")
            else:
                print("Invalid column index!")
        else:
            print("Invalid choice! Please enter 'row' or 'column'.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")


def main():
    # Input dimensions of the matrix
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Create the matrix
    matrix = create_matrix(rows, cols)

    while True:
        print("\nMatrix CRUD Operations:")
        print("1. Read Matrix")
        print("2. Update Matrix")
        print("3. Delete Row/Column")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            read_matrix(matrix)
        elif choice == "2":
            update_matrix(matrix)
        elif choice == "3":
            delete_row_or_column(matrix)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
