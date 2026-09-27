# Evidence for the worked profiles

Retrieved 2026-09-27. [Buyer-facing report](../../worked-area-profiles.md) Â· [Methods](../../worked-area-methods.md).

- `acs-extract.json`: original text estimates and margin fields for nine ACS tables Ã— four areas, plus variable definitions and exact source URLs. 2020â€“2024 ACS, financial amounts in 2024 dollars.
- `derived-measures.json`: 21 measures per area, with formulas/columns and uncertainty. An overlapping measure is not an independent scoring signal.
- `derive.py`: standard-library Python script. Run `python derive.py` from any directory to regenerate the derived file from the included extract. This is limited to the demonstrated sample's field and sentinel cases.
- `render_map.py`: rebuilds the comparison map from the included evidence; requires matplotlib and pyproj.
- `geographies.json`: Census lookup results, ACS 2024 polygons, selected older EPA polygons/fields, public-library address geocodes, and the explicit EPA-selection caveat.
- `retrieval-manifest.json`: exact service queries and hashes of original downloaded responses. These hashes describe the original responses, not the filtered JSON in this folder. Live endpoints can change; reproduce with the saved extract for stable calculations.
- `osm-anchors.json`: separately licensed intersection records. Â© OpenStreetMap contributors, under the [Open Database License 1.0](https://opendatacommons.org/licenses/odbl/1-0/).

To retrieve ACS rows again, stream the table URLs in `acs-extract.json` as UTF-8 pipe-delimited records, preserve their header names, and retain the four exact `GEO_ID` values. Preserve all original strings before decoding special values. API metadata uses names such as `B25024_002E`; the bulk-file equivalent is `B25024_E002`. Do not download the full multi-gigabyte archive to obtain these four rows.

The source extracts are public statistical data and public facility/intersection locations. They do not contain private household inputs. Sources retain their own terms; see the methods document. This evidence bundle is not a production ingestion service or a nationwide data audit.
