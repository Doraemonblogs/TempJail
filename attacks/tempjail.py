from .base import BaseAttack

try:
    from ._tempjail_private import TEMPJAIL as TEMPJAIL
except ImportError:
    class TEMPJAIL(BaseAttack):
        """Public placeholder used until the full attack is released."""

        def __init__(self, cfg):
            super().__init__(cfg)

        def attack(self, image_org, image_tgt, img_index: int = 0):
            raise NotImplementedError(
                "The core TEMPJAIL implementation is withheld in the current public release "
                "and will be open-sourced later."
            )


__all__ = ["TEMPJAIL"]
