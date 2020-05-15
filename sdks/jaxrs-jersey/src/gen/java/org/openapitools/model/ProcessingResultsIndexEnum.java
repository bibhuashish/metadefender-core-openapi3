/*
 * MetaDefender Core
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.model;

import java.util.Objects;
import io.swagger.annotations.ApiModel;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import javax.validation.constraints.*;
import javax.validation.Valid;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * Possible overall and per engine analysis results:   | scan_result_i | scan_result_a                |   |---------------|------------------------------|   | 0             | No Threat Detected           |   | 1             | Infected                     |   | 2             | Suspicious                   |   | 3             | Failed                       |   | 4             | Cleaned / Deleted            |   | 7             | Scan Skipped - Whitelisted   |   | 8             | Scan Skipped - Blacklisted   |   | 9             | Exceeded Archive Depth       |   | 10            | Not Scanned                  |   | 12            | Encrypted Archive            |   | 13            | Exceeded Archive Size        |   | 14            | Exceeded Archive File Number |   | 15            | Password Protected Document  |   | 16            | Exceeded Archive Timeout     |   | 17            | File type Mismatch           |   | 18            | Potentially Vulnerable File  |   | 19            | Canceled                     |   | 20            | Sensitive data found         |   | 21            | Yara Rule Matched            |   | 22            | Potentially Unwanted Program |   | 23            | Unsupported file type        |   | 255           | In Progress                  | 
 */
public enum ProcessingResultsIndexEnum {
  
  NUMBER_0(0),
  
  NUMBER_1(1),
  
  NUMBER_2(2),
  
  NUMBER_3(3),
  
  NUMBER_4(4),
  
  NUMBER_7(7),
  
  NUMBER_8(8),
  
  NUMBER_9(9),
  
  NUMBER_10(10),
  
  NUMBER_12(12),
  
  NUMBER_13(13),
  
  NUMBER_14(14),
  
  NUMBER_15(15),
  
  NUMBER_16(16),
  
  NUMBER_17(17),
  
  NUMBER_18(18),
  
  NUMBER_19(19),
  
  NUMBER_20(20),
  
  NUMBER_21(21),
  
  NUMBER_22(22),
  
  NUMBER_23(23),
  
  NUMBER_255(255);

  private Integer value;

  ProcessingResultsIndexEnum(Integer value) {
    this.value = value;
  }

  @JsonValue
  public Integer getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  @JsonCreator
  public static ProcessingResultsIndexEnum fromValue(Integer value) {
    for (ProcessingResultsIndexEnum b : ProcessingResultsIndexEnum.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }
}
