import sys
import os

cur_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(cur_dir, "ImageEditor"))
sys.path.append(os.path.join(cur_dir, "Input"))

from BatchImageEditor import BatchImageEditor
from Args import Args
from BatchJob import BatchJob
from Help import Help

if len(sys.argv) < 2:
    Help.print_help()

args = Args(sys.argv[1:])

options = args.get_options()

job = BatchJob(options)
editor = BatchImageEditor()

editor.process_images(job)