#
# Warning: this is not strict JSON, this is python to allow inline comment
#

{
    "global": {
        "core:datatype": "cf32",            # The datatype of the recording (here, complex 32-bit float)
        "core:sample_rate": 10000000,       # The sample rate of the recording (10 MHz, here).
        "core:version": "0.0.1",            # Version of the SigMF spec used.
        "core:description": "An example metadafile for a SigMF recording.",
    },

    "capture": [
        # The `capture` object contains a list of segments, sorted by the `sample_start` value
        {
            "core:sample_start": 0,         # The sample index that these parameters take effect.
            "core:frequency": 900000000,    # The center frequency of the recording (900 MHz, here).
            "core:time": "2017-02-01T11:33:17,053240428+01:00",
        },
        {
            "core:sample_start": 100000,    # Mandatory
            "core:frequency": 950000000,    # Now at 950 MHz
        },
    ],

    "annotations": [
        # The `annotations` object contains a list of segments, sorted by the `sample_start` value
        {
            "core:sample_start": 1000000,   # The sample index at which this annotation first applies.
            "core:sample_count": 120000,    # The number of samples that this annotation applies to.
            "core:comment": "Some text comment about stuff happening",
        },
    ],
}
