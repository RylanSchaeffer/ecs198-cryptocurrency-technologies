import importlib
import sys
import imp
import rsa
import os


def printProgress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterations  - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()
    if iteration == total:
        print("\n")

f = open('results.txt', 'w')
passed = []
failed = []
rootdir = os.getcwd()
countr = 0
countw = 0
save_stdout = sys.stdout
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        full = subdir + '/' + file
        if file.endswith('py'):
            countw = countw + 1
            path = os.path.join(rootdir, file)
            person = full.find("Program 1/")
            person = person + 10
            eperson = full.find("/Submission")
            current = full[person:eperson]
            sys.stdout = save_stdout
            printProgress(countw, 27, prefix = 'Grading...', suffix='Complete', barLength=50)
            if file.endswith('Submission.py'):
                name = file[:-3]
                try:
                    submission = imp.load_source(name, full)
                    sys.stdout = open(os.devnull,'w')
                    if rsa.verify(*submission.main()):
                        passed.append(current)
                        countr = countr + 1
                except rsa.pkcs1.VerificationError as exc:
                    failed.append(current + " verification error: " + str(exc))
                except AttributeError as exc:
                    failed.append(current + " attribute error: " + str(exc))
                except ImportError as exc:
                    failed.append(current + "import error: " + str(exc))
                except TypeError as exc:
                    failed.append(current + " type error: " + str(exc))

            else:
                if full.find('grader') != -1 and full.find('Rylan'):
                    continue
                failed.append(current + " wrong file name: " + full[full.find("Program 1")+10:])
sys.stdout = save_stdout
f.write("Total Passed: " + str(countr))
f.write("\nTotal Failed: " + str(countw))
f.write("\nPassed:\n")
for name in passed:
    if name.find('Rylan') == -1:
        f.write(name + '\n')
f.write("\nFailed:\n")
for name in failed:
    if name.find('Rylan') == -1:
        f.write(name + '\n')
f.close()
print "Process Completed"
