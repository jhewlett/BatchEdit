import sys
import os

cur_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(cur_dir, "ImageEditor"))
sys.path.append(os.path.join(cur_dir, "Input"))

from ImageEditor import BatchImageEditor
from Input import Args
from Input import BatchJob
from Input import Help

if len(sys.argv) < 2:
    Help.Help.print_help()

args = Args.Args(sys.argv[1:])

options = args.get_options()

job = BatchJob.BatchJob(options)
editor = BatchImageEditor.BatchImageEditor()

editor.process_images(job)