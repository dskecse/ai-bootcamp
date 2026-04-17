# memclean() removes the model from RAM/VRAM but NOT from disk cache.
# The model will NOT be re-downloaded, it'll reload from disk.

import gc

try:
    import torch
except ImportError:
    torch = None

def memclean():
    """
    Frees RAM/VRAM used by old model objects in Colab/Jupyter.

    * Deletes "model" from memory (but NOT from disk cache — no re-download needed)
    * Runs garbage collection
    * Empties GPU memory cache if available
    """
    # If previous model/tokenizer objects exist, drop them
    for name in ("model", "tokenizer"):
        if name in globals():
            del globals()[name]

    # Free CPU RAM
    gc.collect()

    # GPU memory cleanup (if on GPU)
    if torch is not None and torch.cuda.is_available():
        torch.cuda.empty_cache()

    print("[memclean] Old model removed from RAM. Disk cache untouched — no re-download will occur.")
