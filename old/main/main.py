from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.app import Dog

dog1 = Dog("Leo")
dog1.bark()