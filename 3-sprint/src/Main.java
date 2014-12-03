import java.util.Arrays;

public class Main {
    class Board{
        public static final boolean WHITE = false;
        public static final boolean BLACK = true;

        public static final int MAX_X = 10;
        public static final int MAX_Y = 10;
        public static final int MIN_X = 0;
        public static final int MIN_Y = 0;

        private boolean[][] board = new boolean[MAX_X][MAX_Y];

        public int getNumberOfBlackSquares(){
            return Arrays.deepToString(board).replaceAll("[^t]", "").length();
        }
        public void flip(Position p){
            board[p.x][p.y] = !board[p.x][p.y];
        }
        public boolean getColor(Position p){
            return board[p.x][p.y];
        }
    }

    class Position{
        int x;
        int y;
        public Position(int x, int y){
            this.x = x;
            this.y = y;
        }
        public int getNumberPositon(){
            return x * 10 + y;
        }
        public boolean isValidPosition(){
            return x >= Board.MIN_X && x < Board.MAX_X && y >= Board.MIN_Y  && y < Board.MAX_Y;
        }

        public Position generateNewPositionBasedOnMove(int x, int y){
            return new Position(this.x + x, this.y + y);
        }
    }

    public Board board = new Board();
    public Position myPosition = new Position(0,0);

    public Position[] getAllPossibleNewPositions(){
        return new Position[]{
                myPosition.generateNewPositionBasedOnMove(-2, -1), myPosition.generateNewPositionBasedOnMove(-2, 1),
                myPosition.generateNewPositionBasedOnMove(-1, -2), myPosition.generateNewPositionBasedOnMove(-1, 2),
                myPosition.generateNewPositionBasedOnMove(1, -2), myPosition.generateNewPositionBasedOnMove(1, 2),
                myPosition.generateNewPositionBasedOnMove(2, -1), myPosition.generateNewPositionBasedOnMove(2, 1)
        };
    }

    public Position findNewPosition(){
        Position highest = null;
        for (Position pos : getAllPossibleNewPositions()){
            if (pos.isValidPosition()){
                highest = pos;
                if (board.getColor(myPosition) == board.getColor(pos)){
                    return pos;
                }
            }
        }
        return highest;
    }

    public void move(){
        Position newPos = findNewPosition();
        board.flip(myPosition);
        myPosition = newPos;
    }

    public static void main(String[] args) {
        Main m = new Main();
        for (int x = 0; x < 200; x++){
            m.move();
        }
        System.out.println(m.board.getNumberOfBlackSquares());
    }
}
