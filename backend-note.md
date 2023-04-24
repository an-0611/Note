### Backend note

### System Design basic (Horizontal vs Vertical)

|               |          Horizontal           |          Vertical           |
| :-----------: | :---------------------------: | :-------------------------: |
|   Strength    |           Quantity            |            Scale            |
| Load balance  |             true              |             N/A             |
|   Flexible    |           Resilient           |        Single point         |
| Communication | network call (via RPC2(註 1)) | Inter process communication |
|     Speed     |             Slow              |            Fast             |
|  consistancy  |      Data inconsistancy       |         Consistancy         |
|  Scalibility  |          Scales Well          |       Hardware limit        |

註 1
RPC2 是一個輕量級的遠程過程調用協議（Remote Procedure Call Protocol），它是基於 JSON-RPC 協議的擴展版本。與 JSON-RPC 相比，RPC2 提供了更多的特性和更好的性能，可以更好地滿足一些高級應用的需求。RPC2 支持各種編程語言，可以方便地實現分布式應用。
