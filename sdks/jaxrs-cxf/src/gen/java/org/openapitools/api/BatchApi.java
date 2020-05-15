package org.openapitools.api;

import org.openapitools.model.BatchId;
import org.openapitools.model.BatchResponse;
import org.openapitools.model.InlineResponse400;
import org.openapitools.model.InlineResponse500;

import java.io.InputStream;
import java.io.OutputStream;
import java.util.List;
import java.util.Map;
import javax.ws.rs.*;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;
import org.apache.cxf.jaxrs.ext.multipart.*;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import io.swagger.jaxrs.PATCH;
import javax.validation.constraints.*;
import javax.validation.Valid;

/**
 * MetaDefender Core
 *
 * <p>## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 */
@Path("/")
@Api(value = "/", description = "")
public interface BatchApi  {

    /**
     * Cancel Batch
     *
     * When cancelling a batch, the connected analysis that are still in progress will be cancelled also.   The cancelled batch will be closed.      
     *
     */
    @POST
    @Path("/file/{batchId}/cancel")
    @Produces({ "application/json" })
    @ApiOperation(value = "Cancel Batch", tags={ "batch",  })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Batch cancelled.", response = Object.class),
        @ApiResponse(code = 400, message = "Bad Request (e.g. invalid header, apikey is missing or invalid).", response = InlineResponse500.class),
        @ApiResponse(code = 403, message = "Invalid user information or Not Allowed", response = InlineResponse500.class),
        @ApiResponse(code = 404, message = "Batch not found (invalid id)", response = InlineResponse400.class),
        @ApiResponse(code = 500, message = "Unexpected event on server", response = InlineResponse500.class) })
    public Object batchCancel(@PathParam("batchId") String batchId, @HeaderParam("apikey")   String apikey);

    /**
     * Close Batch
     *
     * The batch will be closed and files can no longer can be added to the current batch.      
     *
     */
    @POST
    @Path("/file/batch/{batchId}/close")
    @Produces({ "application/json" })
    @ApiOperation(value = "Close Batch", tags={ "batch",  })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Batch successfully closed.", response = BatchResponse.class),
        @ApiResponse(code = 400, message = "Bad Request (e.g. invalid header, apikey is missing or invalid).", response = InlineResponse500.class),
        @ApiResponse(code = 403, message = "Invalid user information or Not Allowed", response = InlineResponse500.class),
        @ApiResponse(code = 404, message = "Requests resource was not found.", response = InlineResponse500.class),
        @ApiResponse(code = 500, message = "Unexpected event on server", response = InlineResponse500.class) })
    public BatchResponse batchClose(@PathParam("batchId") String batchId, @HeaderParam("apikey")   String apikey);

    /**
     * Initiate Batch
     *
     * Create a new batch and retrieve the batch_id
     *
     */
    @POST
    @Path("/file/batch")
    @Produces({ "application/json" })
    @ApiOperation(value = "Initiate Batch", tags={ "batch",  })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Batch created successfully.", response = BatchId.class),
        @ApiResponse(code = 400, message = "Bad Request (e.g. invalid header, apikey is missing or invalid).", response = InlineResponse500.class),
        @ApiResponse(code = 403, message = "Invalid user information or Not Allowed", response = InlineResponse500.class),
        @ApiResponse(code = 500, message = "Unexpected event on server", response = InlineResponse500.class) })
    public BatchId batchCreate(@HeaderParam("apikey")   String apikey, @HeaderParam("rule")   String rule, @HeaderParam("user_agent")   String userAgent, @HeaderParam("user-data")   String userData);

    /**
     * Download Signed Batch Result
     *
     * Download digitally signed status report for the entire batch
     *
     */
    @GET
    @Path("/file/batch/{batchId}/certificate")
    @Produces({ "text/plain", "application/json" })
    @ApiOperation(value = "Download Signed Batch Result", tags={ "batch",  })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Signed batch result and certificate are sent back in response body (YAML format)."),
        @ApiResponse(code = 400, message = "Bad Request (e.g. invalid header, apikey is missing or invalid).", response = InlineResponse500.class),
        @ApiResponse(code = 403, message = "Invalid user information or Not Allowed", response = InlineResponse500.class),
        @ApiResponse(code = 404, message = "Requests resource was not found.", response = InlineResponse500.class),
        @ApiResponse(code = 500, message = "Unexpected event on server", response = InlineResponse500.class) })
    public void batchSignedResult(@PathParam("batchId") String batchId, @HeaderParam("apikey")   String apikey);

    /**
     * Status of Batch Analysis
     *
     * Retrieve status report for the entire batch
     *
     */
    @GET
    @Path("/file/batch/{batchId}")
    @Produces({ "application/json" })
    @ApiOperation(value = "Status of Batch Analysis", tags={ "batch" })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Batch progress paginated report (50 entries/page).", response = BatchResponse.class),
        @ApiResponse(code = 400, message = "Bad Request (e.g. invalid header, apikey is missing or invalid).", response = InlineResponse500.class),
        @ApiResponse(code = 403, message = "Invalid user information or Not Allowed", response = InlineResponse500.class),
        @ApiResponse(code = 404, message = "Requests resource was not found.", response = InlineResponse500.class),
        @ApiResponse(code = 500, message = "Unexpected event on server", response = InlineResponse500.class) })
    public BatchResponse batchStatus(@PathParam("batchId") String batchId, @HeaderParam("apikey")   String apikey);
}
