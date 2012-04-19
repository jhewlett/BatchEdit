import Args
import sys
sys.path.append("..\\ImageEditor\\")
from ImageEditor import BatchImageEditor
import BatchJob

args = Args.Args(sys.argv[1:])

options = args.get_options()

job = BatchJob.BatchJob(options)
editor = BatchImageEditor.BatchImageEditor()

editor.process_images(job)