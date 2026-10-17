# Draw.io CLI, Export, and Troubleshooting

This reference preserves the execution details of the official Draw.io Codex
skill while keeping the main skill compact.

## Desktop CLI Discovery

Check the platform before using conversion, layout, or export.

| Platform | Typical executable |
|---|---|
| Windows | `C:\Program Files\draw.io\draw.io.exe` |
| Windows per-user | `%LOCALAPPDATA%\Programs\draw.io\draw.io.exe` |
| macOS | `/Applications/draw.io.app/Contents/MacOS/draw.io` |
| Linux | `drawio` |
| WSL2 | `/mnt/c/Program Files/draw.io/draw.io.exe` |

Use `Get-Command drawio` or `where.exe drawio` on Windows and `command -v
drawio` on macOS/Linux before trying fallback paths. Honor an executable
location already supplied by the user. On Windows, if standard paths fail,
check per-user/machine `App Paths\draw.io.exe` registry entries and Draw.io
Start Menu shortcut targets (including a custom install drive). Resolve the
target and confirm it is an existing executable before invoking it with
PowerShell's `&` call operator. Keep discovery bounded to these known locations;
do not recursively scan every drive or install software implicitly.

Without the Desktop CLI:

- author native Draw.io XML directly
- deliver `.drawio`, or use the optional browser-URL route
- do not claim that Mermaid conversion, ELK layout, or image export succeeded

## Conversion and Layout

Convert Mermaid to native Draw.io:

```bash
drawio -x -f xml -o diagram.drawio diagram.mmd
```

Apply a preset layout to XML:

```bash
drawio -x -f xml --layout verticalFlow -o diagram.drawio diagram.drawio
```

Use custom ELK configuration when a preset is insufficient:

```bash
drawio -x -f xml --layout '[{"layout":"elkLayered","config":{"elk.direction":"RIGHT"}}]' -o diagram.drawio diagram.drawio
```

Reroute edges around fixed nodes:

```bash
drawio -x -f xml --layout libavoid -o diagram.drawio diagram.drawio
```

Do not run `libavoid` after a flow or tree layout.

## Export

Export from a native `.drawio` source:

```bash
drawio -x -f png -e -b 10 -o diagram.drawio.png diagram.drawio
drawio -x -f svg -e -b 10 -o diagram.drawio.svg diagram.drawio
drawio -x -f pdf -e -b 10 -o diagram.drawio.pdf diagram.drawio
```

Key flags:

- `-x`: export or conversion mode
- `-f`: output format
- `-e`: embed the diagram XML
- `-b`: border width
- `-t`: transparent PNG background
- `-s`: scale
- `--width` or `--height`: fit while preserving aspect ratio
- `-a`: export all PDF pages
- `-p`: select one page

Keep both the `.drawio` source and requested export for research figures.

## Browser URL Route

The Draw.io URL stores compressed diagram XML in the URL fragment. Node.js can
create the URL without extra packages:

```javascript
const fs = require("fs");
const zlib = require("zlib");

const xml = fs.readFileSync(process.argv[2], "utf8");
const compressed = zlib
  .deflateRawSync(encodeURIComponent(xml))
  .toString("base64");
const payload = encodeURIComponent(compressed);

console.log(
  "https://app.diagrams.net/?grid=0&pv=0&border=10&edit=_blank#R" +
    payload
);
```

Use `#R` followed by URI-encoded Base64 of raw-deflated URI-encoded XML.
For validation, decode the fragment, Base64-decode and inflate raw bytes, then
URI-decode; the result must equal the original XML, including Unicode labels.
Do not wrap the payload in the older `#create=` JSON envelope. URL generation
is local; opening a web editor still follows the existing external-access scope.

On Windows, write the URL to an `.url` shortcut before opening it. Passing the
URL directly through `cmd.exe start` can truncate its `&` and `#` content.

For very large diagrams, deliver the `.drawio` file instead of relying on a long
browser URL.

## Troubleshooting

| Problem | Response |
|---|---|
| Desktop CLI missing | Check bounded custom-install locations; if absent, author XML and deliver `.drawio` |
| `GPU process isn't usable` during CLI export/conversion | Retry the same local command once with `--disable-gpu`; inspect exit status and the actual output. If it still fails, report the failure and retain the native source |
| Mermaid export crashes | Convert Mermaid to `.drawio`, then export that file |
| Blank Mermaid diagram | Check the diagram-type keyword, node IDs, and quoted labels |
| Layout does nothing | Verify the preset or provide a JSON array for custom ELK |
| Corrupt export | Validate XML and escape special characters |
| Diagram opens blank | Confirm root `id="0"` and layer `id="1" parent="0"`; check parent references and cycles |
| Edge is missing | Check terminals, innermost common container parent, and child `mxGeometry relative="1"` |
| Browser URL opens empty | Use the Windows `.url` shortcut route |
| URL is too long | Deliver the native `.drawio` file |

## Data Handling

Native plugin output is written locally. Local Draw.io Desktop export does not
require a cloud rasterizer. The optional browser URL opens the editor web
application, but the diagram payload is carried in the URL fragment. Use local
files and Desktop export when external requests must be minimized.
