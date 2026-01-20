from paperexporter import PaperExporter

if __name__=="__main__":
    q_filename="examplepdfs\example.pdf"
    a_filename="examplepdfs\example2.pdf"
    exporter = PaperExporter(q_filename,a_filename)
    export_dict=(exporter.prep_export())
    for entry in export_dict:
        print(entry)
