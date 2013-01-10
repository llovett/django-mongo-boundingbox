import mongoengine as mdb

class Point( mdb.Document ):
    position = mdb.GeoPointField()
    title = mdb.StringField( max_length=500 )

    def __unicode__( self ):
        return self.title

