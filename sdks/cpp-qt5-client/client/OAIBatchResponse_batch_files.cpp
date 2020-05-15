/**
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

#include "OAIBatchResponse_batch_files.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBatchResponse_batch_files::OAIBatchResponse_batch_files(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBatchResponse_batch_files::OAIBatchResponse_batch_files() {
    this->initializeModel();
}

OAIBatchResponse_batch_files::~OAIBatchResponse_batch_files() {}

void OAIBatchResponse_batch_files::initializeModel() {

    m_batch_count_isSet = false;
    m_batch_count_isValid = false;

    m_files_in_batch_isSet = false;
    m_files_in_batch_isValid = false;

    m_first_index_isSet = false;
    m_first_index_isValid = false;

    m_page_size_isSet = false;
    m_page_size_isValid = false;
}

void OAIBatchResponse_batch_files::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBatchResponse_batch_files::fromJsonObject(QJsonObject json) {

    m_batch_count_isValid = ::OpenAPI::fromJsonValue(batch_count, json[QString("batch_count")]);
    m_batch_count_isSet = !json[QString("batch_count")].isNull() && m_batch_count_isValid;

    m_files_in_batch_isValid = ::OpenAPI::fromJsonValue(files_in_batch, json[QString("files_in_batch")]);
    m_files_in_batch_isSet = !json[QString("files_in_batch")].isNull() && m_files_in_batch_isValid;

    m_first_index_isValid = ::OpenAPI::fromJsonValue(first_index, json[QString("first_index")]);
    m_first_index_isSet = !json[QString("first_index")].isNull() && m_first_index_isValid;

    m_page_size_isValid = ::OpenAPI::fromJsonValue(page_size, json[QString("page_size")]);
    m_page_size_isSet = !json[QString("page_size")].isNull() && m_page_size_isValid;
}

QString OAIBatchResponse_batch_files::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBatchResponse_batch_files::asJsonObject() const {
    QJsonObject obj;
    if (m_batch_count_isSet) {
        obj.insert(QString("batch_count"), ::OpenAPI::toJsonValue(batch_count));
    }
    if (files_in_batch.size() > 0) {
        obj.insert(QString("files_in_batch"), ::OpenAPI::toJsonValue(files_in_batch));
    }
    if (m_first_index_isSet) {
        obj.insert(QString("first_index"), ::OpenAPI::toJsonValue(first_index));
    }
    if (m_page_size_isSet) {
        obj.insert(QString("page_size"), ::OpenAPI::toJsonValue(page_size));
    }
    return obj;
}

qint32 OAIBatchResponse_batch_files::getBatchCount() const {
    return batch_count;
}
void OAIBatchResponse_batch_files::setBatchCount(const qint32 &batch_count) {
    this->batch_count = batch_count;
    this->m_batch_count_isSet = true;
}

QList<OAIBatchResponse_batch_files_files_in_batch> OAIBatchResponse_batch_files::getFilesInBatch() const {
    return files_in_batch;
}
void OAIBatchResponse_batch_files::setFilesInBatch(const QList<OAIBatchResponse_batch_files_files_in_batch> &files_in_batch) {
    this->files_in_batch = files_in_batch;
    this->m_files_in_batch_isSet = true;
}

qint32 OAIBatchResponse_batch_files::getFirstIndex() const {
    return first_index;
}
void OAIBatchResponse_batch_files::setFirstIndex(const qint32 &first_index) {
    this->first_index = first_index;
    this->m_first_index_isSet = true;
}

qint32 OAIBatchResponse_batch_files::getPageSize() const {
    return page_size;
}
void OAIBatchResponse_batch_files::setPageSize(const qint32 &page_size) {
    this->page_size = page_size;
    this->m_page_size_isSet = true;
}

bool OAIBatchResponse_batch_files::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_batch_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (files_in_batch.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_size_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBatchResponse_batch_files::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI