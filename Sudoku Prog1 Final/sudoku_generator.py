import math,random, pygame, sys, copy

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    #This is the sudoku generator class that creates the sudoku board that we use in the game

    '''
    create a sudoku board - initialize class variables and set up the 2D board
    This should initialize:
    self.row_length       - the length of each row
    self.removed_cells - the total number of cells to be removed
    self.board       - a 2D list of ints to represent the board
    self.box_length       - the square root of row_length

    Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

    Return:
    None
    '''

# this function initializes the sudoku generator object with the empty board
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board =  [["-" for i in range(9)] for j in range(9)]
        self.box_length = int(row_length ** (1 / 2))

    '''
    Returns a 2D python list of numbers which represents the board

    Parameters: None
    Return: list[list]
    '''

#this function is a getter function to return the current board attribute
    def get_board(self):
        return self.board

    '''
    Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

    Parameters: None
    Return: None
    '''
#this function prints the current values of the boards, it was used in development stages
    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")
        print()

    '''
    Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

    Parameters:
    row is the index of the row we are checking
    num is the value we are looking for in the row

    Return: boolean
    '''
#this functions checks if the number being entered by the fill_remaining function is in the row
    def valid_in_row(self, row, num):
        x = self.board
        for i in range(len(x[0])):
            if x[row][i] == num:
                return False
        return True

    '''
    Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

    Parameters:
    col is the index of the column we are checking
    num is the value we are looking for in the column

    Return: boolean
    '''
#this function checks if the number being entered by the fill remaining functino is the col
    def valid_in_col(self, col, num):
        x = self.board
        for i in range(0,len(x)):
            if x[i][int(col)] == num:
                return False
        return True

    '''
    Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    num is the value we are looking for in the box

    Return: boolean
    '''
#this function checks if the number is already in the box
    def valid_in_box(self, row_start, col_start, num):
        x = self.board
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if num == x[i][j]:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

    Parameters:
    row and col are the row index and col index of the cell to check in the board
    num is the value to test if it is safe to enter in this cell

    Return: boolean
    '''
#this function checks if the number is valid in the specific index by utilizing the col, row, and box functions
    def is_valid(self, row, col, num):
        if self.valid_in_col(col, num) and self.valid_in_row(row, num):
            row_start = row//3*3
            col_start = col//3*3
            if self.valid_in_box(row_start, col_start, num):
                return True

        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

    Return: None
    '''
#this function fills one box with integers from 1-9
    def fill_box(self, row_start, col_start):
        z = []
        x = self.board
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                y = random.randint(1, 9)
                if y in z:
                    while y in z:
                        y = random.randint(1, 9)
                z.append(y)
                x[i][j] = y

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

    Parameters: None
    Return: None
    '''
#this function fills the 3 diagonal boxes utilizing the fill box function
    def fill_diagonal(self):
        self.get_board()
        for i in range(0, 9, 3):
            self.fill_box(i, i)



    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    #this function fills in the remaining empty spaces of the complete board
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    #this function calls the diagonal and fill remaining to complete the board
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
        complete = copy.deepcopy(self.board)
        return complete

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    #this function removes the empty spaces randomly dependent upon which difficulty level
    def remove_cells(self):
        z = []
        for i in range(self.removed_cells):
            x = random.randint(0,8)
            y = random.randint(0,8)
            if (x,y) in z:
                while (x,y) in z:
                    y = random.randint(0, 8)
                    x = random.randint(0, 8)
            z.append((x,y))
            self.board[x][y] = 0


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
#this function generates the sudoku generator object and returns the boards to the main function
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    complete_board = sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, complete_board

#this class is the cell class, we didn't utilize this that much, but we do use it to draw when the user selects a box
class Cell:

#this initializes the cell object
    def __init__(self, row, col, screen, removed_board, user_board):
        self.row = row
        self.col = col
        self.screen = screen
        self.removed_board = removed_board
        self.user_board = user_board

#




#this function checks if a specific square is able to be edited
    def can_edit(self, row, col):
        if self.removed_board[row][col] == 0:
             return True
        return False

#this function draws the red outline of where the user has selected a box in the board
    def draw(self):
        if self.can_edit(self.row, self.col):
            surface = self.screen
            pygame.draw.rect(surface, (255,0,0), pygame.Rect(self.col*80, self.row*80, 82, 82), 1)
            pygame.display.flip()
            return True
        return False

#this is the board class, where most of the functionality of the board screen occurs
class Board:

    #this function initializes the the board object where most of the updates to the user_board 2D list occurs
    def __init__(self, width, height, screen, difficulty, removed_board, complete_board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.removed_board = removed_board
        self.user_board = copy.deepcopy(removed_board)
        self.complete_board = complete_board

#this function draws the diagonal lines of the sudoku board
    def draw_lines(self):
        for i in range(0, 10):
            pygame.draw.line(self.screen,
                             (0, 0, 0),
                             (0, i * (self.width / 9)),
                             (self.width, i * (self.width / 9)),
                             2
                             )
            pygame.draw.line(self.screen,
                             (0, 0, 0),
                             (i * (self.width / 9), 0),
                             (i * (self.width / 9), self.width), 2
                             )

        for j in range(0, 9 // 2):
            pygame.draw.line(self.screen,
                             (0, 0, 0),
                             (0, j * (self.width // (9 // 3))),
                             (self.width, j * (self.width // (9 // 3))),
                             5)
            pygame.draw.line(self.screen,
                             (0, 0, 0),
                             (j * (self.width // (9 // 3)), 0),
                             (j * (self.width // (9 // 3)), self.width),
                             5)

#this function draws the board and contains the while loop for the pygame event tracking
    def draw(self):
        #this code below creates the fonts for the buttons and titles
        difficulty_font = pygame.font.Font(None, 40)
        button_font = pygame.font.Font(None, 60)
        num_font = pygame.font.Font(None, 30)

       #this code clears the screen and draws the blue square of the board
        self.screen.fill((255, 255, 255))
        board_rect = self.screen.get_rect(width=(self.width), height=(self.width), x=0, y=0)
        pygame.draw.rect(self.screen, (173, 216, 230), board_rect)

        self.draw_lines()

        #these 4 sections below here create all the buttons and the surfaces
        level_button = difficulty_font.render(f'Difficulty: {self.difficulty}', 0, (0, 0, 0), (255, 165, 0))
        level_position = level_button.get_rect(topleft=(0, self.width + 5))
        self.screen.blit(level_button, level_position)

        reset_button = button_font.render("Reset", 0, (0, 0, 0), (255, 165, 0))
        reset_position = reset_button.get_rect(center=(self.width // 3 // 2, self.height - 50))
        reset_outline_rect = reset_button.get_rect(center=(self.width // 3 // 2 - 5, self.height - 55),
                                                   width=(reset_position.width + 10),
                                                   height=(reset_position.height + 10))
        pygame.draw.rect(self.screen, (0, 0, 0), reset_outline_rect)
        self.screen.blit(reset_button, reset_position)

        restart_button = button_font.render("Restart", 0, (0, 0, 0), (255, 165, 0))
        restart_position = restart_button.get_rect(center=(self.width // 2, self.height - 50))
        restart_outline_rect = restart_button.get_rect(center=(self.width // 2 - 5, self.height - 55),
                                                       width=(restart_position.width + 10),
                                                       height=(restart_position.height + 10))
        pygame.draw.rect(self.screen, (0, 0, 0), restart_outline_rect)
        self.screen.blit(restart_button, restart_position)

        quit_button = button_font.render("Exit", 0, (0, 0, 0), (255, 165, 0))
        quit_position = quit_button.get_rect(center=(self.width - self.width // 3 // 2, self.height - 50))
        quit_outline_rect = quit_button.get_rect(center=(self.width - self.width // 3 // 2 - 5, self.height - 55),
                                                 width=(quit_position.width + 10), height=(quit_position.height + 10))
        pygame.draw.rect(self.screen, (0, 0, 0), quit_outline_rect)
        self.screen.blit(quit_button, quit_position)

        #this section prints out all of the numbers that are apart of the sudoku game and not the empty squares
        for i in range(0, len(self.removed_board)):
            for j in range(0, len(self.removed_board[i])):
                if self.removed_board[i][j]!=0:
                    integer = self.removed_board[i][j]
                    integer = str(integer)
                    num = num_font.render(integer, 0, (0,0,0))
                    cell_pos = num.get_rect(center = (j*80+40, i*80+40))
                    self.screen.blit(num, cell_pos)

        selected = (None, None)
        place = False

        # this is the while loop that checks the users event inputs on the UI
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0]
                    y = event.pos[1]
                    if reset_position.collidepoint(event.pos):
                        self.reset_to_original()
                    elif restart_position.collidepoint(event.pos):
                        main()
                    elif quit_position.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif self.click(x, y)!=None:
                       self.draw_lines()
                       row = self.click(x, y)[0]
                       col = self.click(x, y)[1]
                       selected, edit = self.select(row, col)
                       place = False
                       if edit == False:
                           selected = (None, None)
                if selected != (None, None):
                    if event.type == pygame.KEYDOWN and pygame.key.name(event.key).isdigit() and 0<int(pygame.key.name(event.key))<10:
                        number = pygame.key.name(event.key)
                        self.sketch(number, row, col)
                        place = True
                if place:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.place_number(number, row, col)




            #this is how we exit the board.draw() function back to the main function
            if self.check_board() == True:
                return True
            elif self.check_board() == False:
                return False


            pygame.display.update()


    #this function selects the square and calls the cell draw to draw the red box
    def select(self, row, col):
        cell = Cell(row, col, self.screen, self.removed_board, self.user_board)
        edit = cell.draw()
        return ((row,col)), edit

    #this function checks where the user clicks on the screen
    def click(self, x, y):
        if x <= self.width and y <= self.width:
            row = math.ceil(y//(self.width//9))
            col = math.ceil(x//(self.width//9))
            return (row, col)
        else:
            return None

    #this function resets the board to the original removed squares
    def reset_to_original(self):
        self.draw()
        self.user_board = copy.deepcopy(self.removed_board)

    #this function checks if all spaces have been filled
    def is_full(self):
        for i in range(0, len(self.user_board)):
            for j in range(0, len(self.user_board[i])):
                if self.user_board[i][j] == 0:
                    return False
        return True

    #this function checks if the board is full and wether or not the user board is equal to the completed board
    def check_board(self):
        if self.is_full() == True:
            for i in range(0, len(self.user_board)):
                for j in range(0, len(self.user_board[i])):
                    if self.user_board[i][j] != self.complete_board[i][j]:
                        return False
            return True
        else:
            return None

    #this function sketches the user's note in the top left of the box
    def sketch(self, value, row, col):
        num_font= pygame.font.Font(None, 20)
        num = num_font.render(str(value), 0, (128, 128, 128), (173, 216, 230))
        num_pos = num.get_rect(center = (col*80+15, row*80+15))
        self.screen.blit(num, num_pos)
        pygame.display.flip()

    #this function draws the number in the actual box and deletes the note and updates the user's 2D list
    def place_number(self, value, row, col):
        num_font = pygame.font.Font(None, 30)
        self.sketch("    ", row, col)
        num = num_font.render(value, 0, (0, 0, 0), (173, 216, 230))
        cell_pos = num.get_rect(center=(col * 80 + 40, row * 80 + 40))
        self.screen.blit(num, cell_pos)
        self.user_board[row][col] = int(value)



#this function is in charge of the start screen and its functionality
def start_game(screen, WIDTH, LENGTH):
    screen.fill((255, 255, 255))

    title_font = pygame.font.Font(None, 100)

    button_font = pygame.font.Font(None, 60)

    background_image = pygame.image.load("sudoku.png").convert()

    screen.blit(background_image, (-(WIDTH // 75), LENGTH // 8))

    #these 8 blocks of code create the buttons and titles for the title screen
    title_surface = title_font.render("Welcome to Sudoku!", 0, (0, 0, 0), (165, 107, 70))
    title_position = title_surface.get_rect(center=(WIDTH // 2, LENGTH // 20))
    screen.blit(title_surface, title_position)

    suggestion_surface = button_font.render("Select Game Mode:", 0, (0, 0, 0), (165, 107, 70))
    suggestion_position = suggestion_surface.get_rect(center=(WIDTH // 2, LENGTH - LENGTH // 9))
    screen.blit(suggestion_surface, suggestion_position)

    easy_button = button_font.render("Easy", 0, (0, 0, 0), (255, 165, 0))
    easy_position = easy_button.get_rect(center=(WIDTH // 8, LENGTH - LENGTH // 22))
    easy_outline_rect = easy_button.get_rect(center=(WIDTH // 8 - 5, LENGTH - LENGTH // 22 - 5),
                                             width=(easy_position.width + 10), height=(easy_position.height + 10))
    pygame.draw.rect(screen, (0, 0, 0), easy_outline_rect)
    screen.blit(easy_button, easy_position)

    medium_button = button_font.render("Medium", 0, (0, 0, 0), (255, 165, 0))
    medium_position = medium_button.get_rect(center=(WIDTH // 2, LENGTH - LENGTH // 22))
    medium_outline_rect = medium_button.get_rect(center=(WIDTH // 2 - 5, LENGTH - LENGTH // 22 - 5),
                                                 width=(medium_position.width + 10),
                                                 height=(medium_position.height + 10))
    pygame.draw.rect(screen, (0, 0, 0), medium_outline_rect)
    screen.blit(medium_button, medium_position)

    hard_button = button_font.render("Hard", 0, (0, 0, 0), (255, 165, 0))
    hard_position = hard_button.get_rect(center=(WIDTH - WIDTH // 8, LENGTH - LENGTH // 22))
    hard_outline_rect = hard_button.get_rect(center=(WIDTH - WIDTH // 8 - 5, LENGTH - LENGTH // 22 - 5),
                                             width=(hard_position.width + 10), height=(hard_position.height + 10))
    pygame.draw.rect(screen, (0, 0, 0), hard_outline_rect)
    screen.blit(hard_button, hard_position)

    #this while loop tracks the user input for events on the main screen
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_position.collidepoint(event.pos):
                    return "Easy"
                elif medium_position.collidepoint(event.pos):
                    return "Medium"
                elif hard_position.collidepoint(event.pos):
                    return "Hard"

        pygame.display.update()





#this is the code for the finished screen that checks whether the user has won or lost on the complete board they submitted
def finished_screen(screen, width, length, truth):
    screen.fill((255, 255, 255))

    title_font = pygame.font.Font(None, 100)

    button_font = pygame.font.Font(None, 60)

    background_image = pygame.image.load("sudoku.png").convert()

    screen.blit(background_image, (-(width // 75), length // 8))

    #this checks whether to print a winning or losing screen and which functionality
    if truth:
        phrase = "Game Won!"
        button_phrase = "Exit"
    else:
        phrase = "Game Over :("
        button_phrase = "Restart"

    #these two blocks create the title and the button to be utilized
    title_surface = title_font.render(phrase, 0, (0, 0, 0), (165, 107, 70))
    title_position = title_surface.get_rect(center=(width // 2, length // 20))
    screen.blit(title_surface, title_position)

    quit_button = button_font.render(button_phrase, 0, (0, 0, 0), (255, 165, 0))
    quit_position = quit_button.get_rect(center=(width//2, length - 50))
    quit_outline_rect = quit_button.get_rect(center=(width// 2 - 5, length - 55),
                                                 width=(quit_position.width + 10), height=(quit_position.height + 10))
    pygame.draw.rect(screen, (0, 0, 0), quit_outline_rect)
    screen.blit(quit_button, quit_position)

    #this loop checks which event is utilized by the user on the UI
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_position.collidepoint(event.pos):
                    if truth:
                        pygame.quit()
                        sys.exit()
                    else:
                        main()


        pygame.display.update()



#this is our main function
def main():
    #this is where we create and set up the start screen
    WIDTH = 720
    LENGTH = 850
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, LENGTH))
    pygame.display.set_caption("Sudoku")

    #this checks which difficulty to pass to the board object
    level_chosen = start_game(screen, WIDTH, LENGTH)
    if level_chosen == "Easy":
        remove = 30
    elif level_chosen == "Medium":
        remove = 40
    else:
        remove = 50
    board, complete_board = generate_sudoku(9, remove)


    #this is where we start the game in the board screen and board object
    board = Board(WIDTH, LENGTH, screen, level_chosen, board,complete_board)
    game_function = board.draw()

    #this utilizes what is returned from the board.draw function and calls to the final screen
    finished_screen(screen, WIDTH, LENGTH, game_function)


#this calls the main function to start the game when the file is ran as the main file
if __name__ == "__main__":
    main()