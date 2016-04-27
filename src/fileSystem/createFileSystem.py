import os

class fileSystem(object):
    def __init__(self):
        self.HDD = os.path.join(os.getcwd(), '..', '..', '..', 'HDD')
    
    def createFileSystem(self):
        if not os.path.exists(self.HDD):
            with open(self.HDD, 'wb') as bigfile:
                bigfile.seek(1048575)
                bigfile.write('0')
        else:
            print 'file present'

if __name__ == '__main__':
    f = fileSystem()
    f.createFileSystem()
    print 'done'
