library(shiny)

CMD <- "/home/shu/anaconda2/bin/scrapy"
CRAWL <- "crawl physics"


function(input, output, session) {
  observeEvent(input$crawl, {
    system2(command = CMD, args = CRAWL, stdout = TRUE)
  })
}