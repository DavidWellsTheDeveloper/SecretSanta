import math
import random

def CreateTables(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE Family (
            id integer primary key,
            name text
        );
        """)
    except:
        return False

    cursor.execute("""
    CREATE TABLE Users (
        id integer primary key,
        firstName text,
        lastName text,
        email text,
        FamilyId REFERENCES Family(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE Events (
        id integer primary key,
        eventName text,
        createDate DATETIME DEFAULT CURRENT_TIMESTAMP,
        pairingDate DATETIME,
        modifiedDate DATETIME
    );
    """)

    cursor.execute("""
    CREATE TABLE EventUser (
        id integer primary key,
        isOwner BOOLEAN DEFAULT 0,
        eventId integer REFERENCES Events,
        userId integer REFERENCES Users,
        targetUserId REFERENCES EventUser(id)
    );
    """)

    conn.commit()
    return True

def InsertFamily(cursor, family):
    cursor.execute('INSERT INTO Family ("name") VALUES (?)', family)
    familyId = cursor.lastrowid
    return familyId

def InsertEventUser(cursor, eventUser):
    cursor.execute('INSERT INTO EventUser ("isOwner", "eventId", "userId") VALUES (?,?,?)', eventUser)

def InsertUser(cursor, eventId, userData):
    cursor.execute('INSERT INTO Users ("firstName", "lastName", "email", "familyId") VALUES (?,?,?,?)', userData)
    userId = cursor.lastrowid
    InsertEventUser(cursor, (1, eventId, userId))

def InsertUsers(conn, eventId):
    cursor = conn.cursor()
    familyId = InsertFamily(cursor, ("KathieHall",)) # does Kathie want to be part of RickWells family?
    InsertUser(cursor, eventId, ("Kathie", "Hall", "greenfreak201@gmail.com", familyId))

    familyId = InsertFamily(cursor, ("StephWells",))
    InsertUser(cursor, eventId, ("Stephanie", "Wells", "stephanie.wells4068@gmail.com", familyId))
    InsertUser(cursor, eventId, ("Quill", "Maurer", "kbradley11@msn.com", familyId))

    familyId = InsertFamily(cursor, ("RickWells",))
    InsertUser(cursor, eventId, ("Rick", "Wells", "ricwells4002@gmail.com", familyId))
    InsertUser(cursor, eventId, ("Marion", "Wells", "mairwells1@gmail.com", familyId))
    InsertUser(cursor, eventId, ("Darcy", "Wells", "d.robin.wells@gmail.com", familyId))
    InsertUser(cursor, eventId, ("David", "Wells", "dave1.t.wells@gmail.com", familyId))

    familyId = InsertFamily(cursor, ("SteveWells",))
    InsertUser(cursor, eventId, ("Steve", "Wells", "smwells@comcast.net", familyId))
    InsertUser(cursor, eventId, ("Kathy", "Wells", "kkkwells@comcast.net", familyId))
    InsertUser(cursor, eventId, ("Justin", "Wells", "japewells@gmail.com", familyId))
    InsertUser(cursor, eventId, ("Karen", "Wells", "karen.christine1230@gmail.com", familyId))
    InsertUser(cursor, eventId, ("Chelsi", "Wells", "cjwells74@gmail.com", familyId))
    conn.commit()

def InitDB(conn):
    CreateTables(conn)
    
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Events ("eventName") VALUES ("Christmas")')
    eventId = cursor.lastrowid
    conn.commit()

    InsertUsers(conn, eventId)


def CreatePairings(conn):
    cursor = conn.cursor()

    cursor.execute("""
    SELECT u.id, u.firstName, u.LastName, u.email, f.name, e.EventName 
    FROM Users AS u 
    INNER JOIN Family AS f ON u.familyId=f.id
    INNER JOIN EventUser AS eu ON u.id=eu.userId
    INNER JOIN Events AS e ON eu.eventId=e.id
    WHERE e.EventName='Christmas'
    """)
    rows = cursor.fetchall()

    numRows = len(rows)
    failed = True
    while failed:
        failed = False
        targetNumList = set()
        for i in range(numRows):
            santaRow = rows[i]

            matchMade = False
            failCount = 0
            while not matchMade:
                targetNum = math.trunc(random.random() * numRows)
                targetRow = rows[targetNum]
                if targetRow['id'] == santaRow['id']: # target is same as santa
                    matchMade = False
                elif targetNum in targetNumList: # target already has a santa
                    matchMade = False
                elif targetRow['name'] == santaRow['name']: # family of target is same as family of santa
                    matchMade = False
                else:
                    cursor.execute("UPDATE EventUser SET TargetUserId=? WHERE UserId=?", (targetRow['id'], santaRow['id']))
                    conn.commit()
                    targetNumList.add(targetNum)
                    matchMade = True

                if not matchMade:
                    # sometimes we end up with the only remaining target is the santa we are pairing.
                    # in those cases we need to redo the pairings from scratch
                    failCount += 1
                    if failCount>100:
                        matchMade = True
                        failed = True
                        inClause = ""
                        for failRow in rows:
                            if len(inClause)>0:
                                inClause += ", "
                            inClause += str(failRow['id'])
                        query = "UPDATE EventUser SET TargetUserId=NULL WHERE UserId IN (" + inClause + ")"
                        cursor.execute(query)
