public abstract class Tile {

    int tileCoordinate;

    //Constructor
    Tile(int tileCoordinate){
        this.tileCoordinate = tileCoordinate;
    }

    //abstract function to tell us if tile is occupied
    public abstract boolean isTileOccupied();

    // abstract function to get the piece off of a given tile
    public abstract Piece getPiece();

    public static final class EmptyTile extends Tile {

        //constructor for EmptyTile
        EmptyTile(int coordinate){
            super(coordinate);
        }

        @Override
        public boolean isTileOccupied() {
            return false;
        }

        @Override
        public Piece getPiece() {
            return null;
        }
    }

    public static final class OccupiedTile extends Tile{

        // member variable is the actual piece itself
        Piece pieceOnTile;

        //Constructor for OccupiedTile
        OccupiedTile(int tileCoordinate, Piece pieceOnTile){
            super(tileCoordinate);
            this.pieceOnTile = pieceOnTile;
        }

        @Override
        public boolean isTileOccupied() {
            return true;
        }

        @Override
        public Piece getPiece() {
            return this.pieceOnTile;


    }
}

