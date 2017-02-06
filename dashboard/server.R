library(shiny)

CMD <- "/home/shu/anaconda2/bin/scrapy"
CRAWL <- "crawl get_email"

system2(command = CMD, args = "bench")

function(input, output, session) {
  observeEvent(input$crawl, {
    system2(command = CMD, args = CRAWL, stdout = TRUE)
  })
}