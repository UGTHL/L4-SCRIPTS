import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))
