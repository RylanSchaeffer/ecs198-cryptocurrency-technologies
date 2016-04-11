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

f = open('results.txt', 'w') #write out results in results.txt
passed = []
failed = []
rootdir = os.getcwd()
countr = 0
countw = 0
count = 0
save_stdout = sys.stdout #save output object so we can redirect students output to dev/null
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        full = subdir + '/' + file #create full path
        if file.endswith('py'): #grab all python files in case they named incorrectly
            if full.find('grader') != -1 and full.find('Rylan'): #skip instructor files
                continue
            count = count + 1 #count for progress bar
            path = os.path.join(rootdir, file)
            person = full.find("Program 1/")
            person = person + 10
            eperson = full.find("/Submission")
            current = full[person:eperson]
            sys.stdout = save_stdout
            printProgress(count, 23, prefix = 'Grading...', suffix='Complete', barLength=50)
            sys.stdout = open(os.devnull,'w') #send student output to devnull

            if file.endswith('Submission.py'): #Correct file formatting
                name = file[:-3]
                try:
                    submission = imp.load_source(name, full)
                    if rsa.verify(*submission.main()):
                        passed.append(current)
                        countr = countr + 1
                except rsa.pkcs1.VerificationError as exc:
                    countw = countw + 1
                    failed.append(current + " verification error: " + str(exc)) #didn't verify correctly
                except AttributeError as exc:
                    countw = countw + 1
                    failed.append(current + " attribute error: " + str(exc))
                except ImportError as exc:
                    countw = countw + 1
                    failed.append(current + "import error: " + str(exc))
                except TypeError as exc:
                    countw = countw + 1
                    failed.append(current + " type error: " + str(exc))
                except:
                    countw = countw + 1
                    failed.append(current + " unexpected [other] error")

            else: #grade for wrong naming 
                name = file[:-3]
                try:
                    submission = imp.load_source(name, full)
                    if rsa.verify(*submission.main()):
                        failed.append('FUNCTIONAL but wrong name: ' + current)
                except rsa.pkcs1.VerificationError as exc:
                    countw = countw + 1
                    failed.append(current + " verification error: " + str(exc))
                except AttributeError as exc:
                    countw = countw + 1
                    failed.append(current + " attribute error: " + str(exc))
                except ImportError as exc:
                    countw = countw + 1
                    failed.append(current + "import error: " + str(exc))
                except TypeError as exc:
                    countw = countw + 1
                    failed.append(current + " type error: " + str(exc))
                except:
                    countw = countw + 1
                    failed.append(current + " unexpected [other] error")
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
sys.exit(0)
